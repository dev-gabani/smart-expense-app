import glob

files = ['templates/home.html', 'templates/view_expenses.html', 'templates/smart_budget.html', 'templates/suggestions.html', 'templates/prediction.html']
block = '''{% block topbar_actions %}
<form method="get" id="monthForm" style="display: flex; align-items: center; gap: 0.5rem; background: var(--bg-card); padding: 0.25rem 0.75rem; border-radius: 8px; border: 1px solid rgba(42,31,24,0.1);">
    <i class="fa-regular fa-calendar" style="color: var(--text-secondary);"></i>
    <input type="month" name="month" value="{{ selected_month }}" onchange="document.getElementById('monthForm').submit()" style="background: transparent; border: none; outline: none; color: var(--text-primary); font-weight: 500; cursor: pointer;">
</form>
{% endblock %}'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if '{% block title %}' in content and 'id="monthForm"' not in content:
        parts = content.split('{% endblock %}', 1)
        new_content = parts[0] + '{% endblock %}\n\n' + block + parts[1]
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
print('Month selector added')
