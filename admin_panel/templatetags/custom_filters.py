from django import template
import datetime
from django.utils.safestring import mark_safe
register = template.Library()




# template filter for date filter
@register.filter
def abbreviate_month(date):
    if isinstance(date, datetime.date):
        return date.strftime('%d %b %Y')
    return date


# template filter to access dictionary values by key
@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)



@register.filter
def index(sequence, position):
    try:
        return sequence[position]
    except IndexError:
        return None
    

# model fields active or inactive 
# @register.filter(name='active_inactive')
# def active_inactive(value):
#     return "Active" if value else "Inactive"


@register.filter(name='active_inactive')
def active_inactive(value):
    if value:
        return mark_safe('<span class="badge bg-success ">Active</span>')
    else:
        return mark_safe('<span class="badge bg-danger ">Inactive</span>')
    



# for pages pagination 
@register.filter
def page_window(current_page, total_pages, visible=5):
    half = visible // 2
    start = max(current_page - half, 1)
    end = min(current_page + half, total_pages)

    # Adjust if near start or end
    if current_page <= half:
        end = min(visible, total_pages)
    elif current_page + half > total_pages:
        start = max(total_pages - visible + 1, 1)

    return range(start, end + 1)

