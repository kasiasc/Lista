 import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'tango_with_django_project.settings')

import django
    django.setup()
    from rango.models import Product, List

def populate():
    
	list_1 = [
        {"title": "lista na wtorek",
        "number": 2}]

    list_2 = [
        {"title": "lista na jutro",
        "number": 3}]

		
    lists = {"Poniedzialek": {"lists": list_1 },
    "Wtorek": {"lists": list_2}}

 
 for prod, prod_data in prods.items():
 c = add_prod(prod)
 for p in prod_data["pages"]:
 add_page(c, p["title"], p["url"])

 # Print out the categories we have added.
 for c in Category.objects.all():
 for p in Page.objects.filter(category=c): 
 print("- {0} - {1}".format(str(c), str(p)))
 def add_page(cat, title, url, views=0):
 p = Page.objects.get_or_create(category=cat, title=title)[0]
 p.url=url
 p.views=views
 p.save()
 return p

 def add_cat(name):
 c = Category.objects.get_or_create(name=name)[0]
 c.save()
 return c

 # Start execution here!
 if __name__ == '__main__':
 print("Starting Rango population script...")
 populate()