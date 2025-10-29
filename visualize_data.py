import pandas as pd
import matplotlib.pyplot as plt

# Load sample dataset
data = pd.DataFrame({
    'Product': ['Product A', 'Product B', 'Product C'],
    'Sales': [150, 200, 100]
})

# Plot visualization
plt.bar(data['Product'], data['Sales'])
plt.title('E-Commerce Sales Data')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.show()
