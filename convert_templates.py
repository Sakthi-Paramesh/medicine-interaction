import os
import re

TEMPLATE_DIR = 'templates'

# 1. Break layout.html into parts
layout_path = os.path.join(TEMPLATE_DIR, 'fragments', 'layout.html')
with open(layout_path, 'r', encoding='utf-8') as f:
    layout_content = f.read()

# Extract header
header_match = re.search(r'<head th:fragment="header\(title\)">(.+?)</head>', layout_content, re.DOTALL)
header_content = """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - HumanEase AI</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    <!-- Bootstrap Icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
</head>"""

navbar_content = """{% load static %}
<nav class="navbar navbar-expand-lg navbar-custom">
    <div class="container">
        <a class="navbar-brand" href="{% url 'index' %}">
            <i class="bi bi-shield-plus text-primary me-2"></i>HumanEase AI
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto align-items-center">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'index' %}">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'search' %}">Search</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'scanner' %}"><i class="bi bi-camera me-1"></i>Scanner</a>
                </li>
                {% if not user.is_authenticated %}
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'login' %}">Login</a>
                </li>
                <li class="nav-item ms-lg-2">
                    <a class="btn btn-primary-custom" href="{% url 'register' %}">Sign Up</a>
                </li>
                {% else %}
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'dashboard' %}">Dashboard</a>
                </li>
                <li class="nav-item ms-lg-2">
                    <form action="{% url 'logout_api' %}" method="post" class="d-inline" id="logoutForm">
                        {% csrf_token %}
                        <button type="button" onclick="logout()" class="btn btn-outline-custom">Logout</button>
                    </form>
                </li>
                {% endif %}
                <li class="nav-item ms-3">
                    <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" id="theme-toggle">
                        <label class="form-check-label" for="theme-toggle"><i class="bi bi-moon-stars"></i></label>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>

<script>
    function logout() {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        fetch('{% url "logout_api" %}', { 
            method: 'POST',
            headers: { 'X-CSRFToken': csrfToken }
        })
        .then(response => {
            window.location.href = '{% url "login" %}?logout';
        });
    }
</script>
"""

footer_content = """{% load static %}
<div class="mt-auto py-4 text-center border-top">
    <div class="container">
        <p class="text-muted-custom mb-0">&copy; 2026 Sakthi Paramesh HumanEase. All rights reserved.</p>
    </div>
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Custom JS -->
    <script src="{% static 'js/main.js' %}"></script>
</div>
"""

with open(os.path.join(TEMPLATE_DIR, 'fragments', 'header.html'), 'w', encoding='utf-8') as f:
    f.write(header_content)
with open(os.path.join(TEMPLATE_DIR, 'fragments', 'navbar.html'), 'w', encoding='utf-8') as f:
    f.write(navbar_content)
with open(os.path.join(TEMPLATE_DIR, 'fragments', 'footer.html'), 'w', encoding='utf-8') as f:
    f.write(footer_content)

# Delete layout.html
os.remove(layout_path)

def convert_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Load static if needed
    if 'th:href' in content or 'th:src' in content or 'layout ::' in content:
        content = '{% load static %}\n' + content

    # Layout replacements
    content = re.sub(r'<head th:replace="~\{fragments/layout :: header\(\'([^\']+)\'\)\}"></head>', 
                     r"{% include 'fragments/header.html' with title='\1' %}", content)
    content = re.sub(r'<div th:replace="~\{fragments/layout :: navbar\}"></div>', 
                     r"{% include 'fragments/navbar.html' %}", content)
    content = re.sub(r'<div th:replace="~\{fragments/layout :: footer\}"></div>', 
                     r"{% include 'fragments/footer.html' %}", content)
    
    # URL replacements th:href="@{/path}"
    # Wait, simple mapping for known URLs:
    url_map = {
        '/': 'index',
        '/login': 'login',
        '/register': 'register',
        '/dashboard': 'dashboard',
        '/search': 'search',
        '/scanner': 'scanner',
        '/saved': 'saved_medicines',
        '/interaction': 'interaction',
        '/medicine/ai': 'medicine_ai_detail',
    }
    
    def repl_href(m):
        path = m.group(1)
        if path.startswith('/css/') or path.startswith('/images/') or path.startswith('/js/'):
            return f'href="{{% static \'{path[1:]}\' %}}"'
        elif path in url_map:
            return f'href="{{% url \'{url_map[path]}\' %}}"'
        return f'href="{path}"'

    content = re.sub(r'th:href="@{([^}]+)}"', repl_href, content)
    
    def repl_src(m):
        path = m.group(1)
        return f'src="{{% static \'{path[1:]}\' %}}"'
        
    content = re.sub(r'th:src="@{([^}]+)}"', repl_src, content)
    
    # Other th: attributes
    content = re.sub(r'xmlns:th="http://www.thymeleaf.org"', '', content)
    
    # Variables th:text="${var}"
    content = re.sub(r'th:text="\$\{([^}]+)\}"', r'>{{ \1 }}<', content)
    # Fix the tags if it replaced the attribute inside
    # Basically `<span th:text="${username}">User</span>` became `<span >{{ username }}<User</span>`
    # Let's fix this properly.
    content = re.sub(r'th:text="\$\{([^}]+)\}"([^>]*)>.*?</([^>]+)>', r'\2>{{ \1 }}</\3>', content)

    # Some remaining cleanup
    content = content.replace("th:action", "action")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for root, _, files in os.walk(TEMPLATE_DIR):
    for f in files:
        if f.endswith('.html') and f not in ['header.html', 'navbar.html', 'footer.html']:
            convert_file(os.path.join(root, f))

print("Conversion script complete.")
