import flet as ft

def main(page: ft.Page):
    page.title = "BarberApp - Kalendarz Wizyt"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Prosta lista wizyt
    wizyty = ft.ListView(expand=True, spacing=10)

    def dodaj_wizyte(e):
        if pole_imie.value != "":
            wizyty.controls.append(ft.Text(f"Wizyta: {pole_imie.value}"))
            pole_imie.value = ""
            page.update()

    pole_imie = ft.TextField(label="Imię klienta", width=300)
    przycisk = ft.ElevatedButton("Dodaj wizytę", on_click=dodaj_wizyte)

    page.add(
        ft.Text("Zapisy u Barbera", size=30, weight=ft.FontWeight.BOLD),
        pole_imie,
        przycisk,
        ft.Divider(),
        wizyty
    )

ft.app(target=main)