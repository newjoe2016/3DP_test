from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import sys


# Create a new plot
name = str(sys.argv[1])
B_s = str(sys.argv[2])

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Load the STL files and add the vectors to the plot
path1 = '/home/mrzhou/Printer_v3/Printer/file/stl_file/'
path = path1+name+'.'+B_s
#paths = path1+name+'.stl'


your_mesh = mesh.Mesh.from_file(path)

'''except:

	your_mesh = mesh.Mesh.from_file(paths)

else:
	print("else except")'''


axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Auto scale to the mesh size
scale = your_mesh.points.flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)



volume, cog, inertia = your_mesh.get_mass_properties()
print("Volume                                  = {0}".format(volume))

print(min(scale))
print(max(scale))
# Show the plot to the screen

path2 = '/home/mrzhou/Printer_v3/Printer/file/stl_file/stl_image/'
path2 = path2 + name+'.png'

pyplot.savefig(path2)