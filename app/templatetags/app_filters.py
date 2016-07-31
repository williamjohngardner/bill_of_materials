from django import template
register = template.Library()


@register.filter(name="part_sum")
def part_sum(your_list):
  return sum(d.cost for d in your_list)
 
