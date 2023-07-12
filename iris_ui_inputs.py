"""
Purpose: Provide user interaction options for the MT Cars dataset.

IDs must be unique. They are capitalized in this app for clarity (not typical).
The IDs are case-sensitive and must match the server code exactly.
Preface IDs with the dataset name to avoid naming conflicts.

"""
from shiny import ui


def get_iris_inputs():
    return ui.panel_sidebar(
        ui.h2("Iris Interaction"),
        ui.tags.hr(),
        ui.input_slider(
            "sepal.length",
            "Sepal Length",
            min=4,
            max=8,
            value=[4, 8],
        ),
        ui.input_slider(
        "petal.length",
        "Petal Length",
        min=1,
        max=7,
        value=[1, 7],
        ),  # End of sidebar
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Iris Table"),
            ui.tags.p("Description of each field in the table:"),
            ui.tags.ul(
                ui.tags.li("sepal.length: Sepal length, in cm"),
                ui.tags.li("sepal.width: Sepal width, in cm"),
                ui.tags.li("petal.length: Petal length, in cm"),
                ui.tags.li("petal.width: Petal width, in cm"),
                ui.tags.li("variety: Iris variety"),
            ),
            ui.output_table("iris_table"),
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )
