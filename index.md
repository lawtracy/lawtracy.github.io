---
layout: default
title: Home
---

<!-- Include site header -->
{% include header.html %}

<!-- Posts list -->
<div class="container">
    <div class="posts-list">
        {% unless paginator.posts.empty? %}
            {% for post in paginator.posts %}
                {% include post-card.html %}
            {% endfor %}
        {% else %}
            <p>No posts yet. Check back soon!</p>
        {% endunless %}
    </div>
</div>

<!-- Pagination -->
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
