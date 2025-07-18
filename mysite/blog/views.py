from django.shortcuts import render
import plotly.express as px
import pandas as pd

# Main blog pages
def blog(request):
    return render(request, 'blog/index.html')

def blog_more1(request):
    return render(request, 'blog/blogmore1.html')

def blog_more2(request):
    return render(request, 'blog/blogmore2.html')

def blog_more3(request):
    return render(request, 'blog/blogmore3.html')



# Global map view using Plotly
def map_view(request):
    # Sample city data for demonstration
    df = pd.DataFrame({
        'City': ['London', 'New York', 'Tokyo'],
        'Latitude': [51.5074, 40.7128, 35.6762],
        'Longitude': [-0.1278, -74.0060, 139.6503],
    })

    # Create the Plotly scatter map
    fig = px.scatter_geo(
        df,
        lat='Latitude',
        lon='Longitude',
        text='City',
        projection='natural earth',
        title='World Cities'
    )
    
    # Convert Plotly figure to HTML
    map_html = fig.to_html(full_html=False)

    # Pass it to the template
    return render(request, 'blog/map.html', {'map_html': map_html})
