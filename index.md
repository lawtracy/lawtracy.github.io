---
layout: default
title: Home
---

<!-- Posts list with proper container -->
<div class="container">
    {% for post in paginator.posts %}
        {% include post-card.html %}
    {% endfor %}
</div>

<!-- Pagination with proper container -->
{% if paginator.total_pages > 1 %}
    <nav class="pagination">
        <div class="container">
            {% if paginator.previous_page %}
                <a href="{{ paginator.previous_page_path | relative_url }}" class="pagination-prev">← Previous</a>
            {% endif %}
            
            <span class="pagination-info">
                Page {{ paginator.page }} of {{ paginator.total_pages }}
            </span>
            
            {% if paginator.next_page %}
                <a href="{{ paginator.next_page_path | relative_url }}" class="pagination-next">Next →</a>
            {% endif %}
        </div>
    </nav>
{% endif %}