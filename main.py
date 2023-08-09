from bs4 import BeautifulSoup

# List of HTML file paths to combine
html_files = ['boxplot_EBLEN.html', 'boxplot_LIFNR.html','isolation_forest_plot.html','kmeans_plot.html','pdf_plot_EBLEN.html','pdf_plot_LIFNR.html','rsf_plot_EBLEN.html','ZSCORE_EBLEN.html','rsf_plot_LIFNR.html','rsf_plot_LIFNR.html']

# Create a BeautifulSoup object to hold the combined content
combined_html = BeautifulSoup(features="html.parser")

# Iterate over the HTML files
for file in html_files:
    # Open each file and read its contents with the appropriate encoding
    with open(file, 'r', encoding='utf-8') as f:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(f, 'html.parser')
        
        # Append the contents of the parsed HTML to the combined_html object
        combined_html.append(soup)

# Save the combined HTML to a new file
combined_file_path = 'combined.html'
with open(combined_file_path, 'w', encoding='utf-8') as f:
    f.write(combined_html.prettify())

# Display a message with the file path of the combined HTML file
print("Combined HTML file saved at:", combined_file_path)
