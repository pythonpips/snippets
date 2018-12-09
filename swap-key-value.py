"""author: @pythonpips"""

contact = {'name': 'Vaibhav', 'phone': '+111111111111', 'skills': 'Python'}

swapped_contact_dict = {value:key for key, value in contact.items()}

"""swapped_contact_dict outputs: 
{'Python': 'skills', 'Vaibhav': 'name', '+111111111111': 'phone'}
"""
