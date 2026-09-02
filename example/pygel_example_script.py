from pygel3d import hmesh, gl_display as gl, graph

# Loading igea mesh example 
m = hmesh.load("bunny.obj")

# Ensuring mesh loaded correctly
assert m is not None, "Failed to load mesh"


# Checking number of vertics and faces in mesh
print(f'Number of vertices: {len(m.vertices())}')
print(f'Number of faces: {len(m.faces())}')

# Setting up mesh viewer
v = gl.Viewer()

# Displaying loaded igea object
v.display(m) # press esc to exit the viewer

# Very complex mesh
# Simplifying with quadric (press esc once to view the simplified mesh in the viewer)
hmesh.quadric_simplify(m, 0.1) # 10% of the original mesh
v.display(m)
# Notice the holes on the bottom of the bunny.

# If any holes are present in the mesh, we can close them:
hmesh.close_holes(m)
v.display(m)

# After closing holes, it is no longer a triangle mesh, but a polygonal mesh.
# We re-triangulate the mesh to convert it back
hmesh.triangulate(m)
v.display(m)

# Some triangles doesn't look too good. We improve this by maximixing the minimum angle of the triangles
hmesh.maximize_min_angle(m, 0.95) # if 1.0 it only improves triangles that are completely planar
v.display(m)



#### Skeletonization #####
g = graph.from_mesh(m) # convert mesh to graph
# Displaying graph in viewer in x-ray mode
v.display(m, g, mode='x')

# Skeletonization of the graph
s = graph.LS_skeleton(g)
# Displaying the skeleton
v.display(m, s, mode='x') # s itself is a graph.



