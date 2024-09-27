import flet as ft


def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.bgcolor = "purple"
    
    txtpeso=ft.TextField(label="Ingresa tu peso")
    txtaltura=ft.TextField(label="Ingresa tu altura")
    lblIMC=ft.Text("tu IMC es: ")
    
    img=ft.Image(src="https://github.com/Prod-luis1986/Recursos/blob/main/bascula.png",
                width=200,
                height=200
                
                )
    btnCalcular=ft.ElevatedButton(text="Calcular")
    btnlimpiar=ft.ElevatedButton(text="Limpiar")
    
    
    page.add(
        ft.Column(
            controls=[txtpeso,
                      txtaltura,
                      lblIMC
                      ],alignment="CENTER"),
        ft.Row(
            controls=[
                img
            ],alignment="CENTER"),
            ft.Row(
                controls=[
                    btnCalcular,
                    btnlimpiar
                    ],alignment="CENTER")
    )
ft.app(main)
