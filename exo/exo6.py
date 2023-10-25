import datetime

maintenant = datetime.datetime.now()
print("Date et heure actuelles : ", maintenant)
format_personnalise = "%d-%m-%Y %H:%M:%S"
date_formattee = maintenant.strftime(format_personnalise)
print("Date et heure formatées : ", date_formattee)
