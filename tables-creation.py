import numpy as np
import pandas as pd

factor = np.sqrt(2/(3*np.sqrt(3)))
#Initial data of vertices and cells
# no need data_lij0 = np.loadtxt('initial_state/99.txt')
#df = pd.DataFrame(data_lij0, columns=["vertex i", "adj vertex j (>i)", "length","rest length", "VM tension","None A","None B" ])
#df = df.drop(["rest length", "VM tension","None A","None B"], axis=1)

junctions = np.loadtxt('199.txt')
df = pd.DataFrame(junctions, columns=["vertex i", "vertex j", "lij","l0ij","Tij","s1","s2"])
df = df.drop([ "s1","s2"], axis=1)
df["vertex i"] = df["vertex i"].astype(int)
df["vertex j"] = df["vertex j"].astype(int)
df.to_csv("junctions_data.csv")


celdas = np.loadtxt('199_celda.txt').astype(int)
df = pd.DataFrame(celdas, columns=["cell id", "vertex id"])
df.to_csv("cell_vertex_id.csv")


data = np.loadtxt('199_vertices.txt')
df = pd.DataFrame(data, columns=["vertex id","s1", "x", "y","s2","s3","s4","s5"])
df['x'] = df['x']*factor
df['y'] = df['y']*factor
df = df.drop([ "s1","s2","s3","s4","s5"], axis=1)
df["vertex id"] = df["vertex id"].astype(int)
df.to_csv("vertex_data.csv")


top_vtipo1 = np.loadtxt('after2_adys_adys1_cells_vs_tipo1.txt', dtype =float).astype(int)

df = pd.DataFrame(top_vtipo1,columns=["vertex i", "adj 1", "adj 2", "adj 3","adj 11", "adj 21", "adj 31","s1","s2", "cell 1","cell 2","cell 3","s3"])
df = df.drop([ "adj 11", "adj 21", "adj 31", "s1", "s2", "s3"], axis=1)
df.to_csv("adjacents_vertices_cells.csv")
