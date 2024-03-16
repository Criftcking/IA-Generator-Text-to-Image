from win10toast import ToastNotifier

# Crear un objeto ToastNotifier
toaster = ToastNotifier()

# Mostrar una notificación emergente
toaster.show_toast("Mensaje", "You must wait 15 seconds until the API is restored. The browser will close automatically.")
toaster.show_toast("Mensaje", "Debes esperar 15 segundos hasta que se restablesca la API. El navegador se cerrara automaticamente")

