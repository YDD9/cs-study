from xs2ml import xs2ml
import os
print os.getcwd()
# xs2ml takes the XLS filename as an argument on __init__.
x = xs2ml("excel2pdf/test.xls")

# Give this method the root node name and it's attribute-values, if any.
x.create_root_node("PIES", xmlns="http://www.aftermarket.org/eCommerce/Pies")

# Create our basic node structure. This method takes in the target parent node
# and the node names that need to be created under it. We'll get a list in return.
root_nodes = x.add_nodes(x.dom_.firstChild, "Header", "Items", "Trailer")