from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

# Create a new plot
def stl_anylasis():
	figure = pyplot.figure()
	axes = mplot3d.Axes3D(figure)

	# Load the STL files and add the vectors to the plot
	your_mesh = mesh.Mesh.from_file('circle.STL')
	axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

	# Auto scale to the mesh size
	scale = your_mesh.points.flatten(-1)
	axes.auto_scale_xyz(scale, scale, scale)



	volume, cog, inertia = your_mesh.get_mass_properties()
	print("Volume                                  = {0}".format(volume))

	print(min(scale))
	print(max(scale))
	# Show the plot to the screen
	#pyplot.savefig('foo.png')
	pyplot.show()

stl_anylasis()