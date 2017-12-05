
using DataFrames, LowRankModels
using CSV

Current = readtable("NYSE Delta_vol.csv");
size(Current)

# generate observations
obs_mat = zeros(size(Current[:,2:2715])) # matrix of observations (1 for observed, 0 otherwise)
Ω = Tuple{Int64,Int64}[]      # list of observations Ω
for i = 1:34
    for j in 2:2715
        if !(isna(Current[i,j]))
            obs_mat[i,j-1]=1
            push!(Ω, (i, j-1))
        else
            Current[i,j]=0
        end
    end
end

current_array = Array(Current[:,2:2715]);

# fit model
loss = HuberLoss()
nonneg = NonNegConstraint()
k = 10
glrm = GLRM(current_array, loss, nonneg, nonneg, k, obs=Ω);

# predict Current_hat
X,W,ch = fit!(glrm);
Current_hat = X'*W;

Current_fixed = current_array+Current_hat.*(1.-obs_mat);
current_fixed = convert(DataFrame,Current_fixed);
current_fixed

CSV.write("NYSE Delta_vol_fixed.csv", current_fixed)
