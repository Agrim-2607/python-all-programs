def dfs(node,res,vis,adj):
    vis[node]=1
    res.append(node)
    for n in adj[node]:
        if vis[n]==0:
            dfs(n,res,vis,adj)

no_of_nodes=8
adj=[[],[2,4],[1,3,6],[2],[1,5,7],[4,8],[2],[4,8],[5,7]]
vis=[0]*(no_of_nodes+1)
res=[]
dfs(1,res,vis,adj)
print(res)