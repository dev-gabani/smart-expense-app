import glob

files = glob.glob('templates/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'id="monthForm"' in content and 'fa-file-csv' not in content:
        # We append the export button right after the form
        new_content = content.replace('</form>\n{% endblock %}', '</form>\n<a href="/export/csv?month={{ selected_month }}" class="btn" style="background: var(--bg-card); color: var(--accent); border: 1px solid rgba(217, 127, 62, 0.3); padding: 0.25rem 0.75rem; border-radius: 8px; font-size: 0.875rem; text-decoration: none; display: flex; align-items: center; gap: 0.5rem;"><i class="fa-solid fa-file-csv"></i> Export</a>\n{% endblock %}')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
print('Export button added')
