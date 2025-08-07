from nicegui import ui

state = {'displayed': False}
sim_controls_column = None  # will hold the dynamic controls
# ui.sub_pages({'/intern_temp': lambda:intern_temp.int_temp()})
from components import (
    intern_temp,
    home,
    altitude,
    acceleration,
    angularRate,
    LiveVideo,
    magneticField,
    map,
    AllChart,
)
global ind
Temperature = [
    12.5,
    137.8,
    12.5,
    90.8,
    33.5
]
Time = [
    1,
    2,
    3,
    4,
    5
]
def charts():
     with ui.grid(columns=2).style("""
                                    position: absolute;
                                    left: 200px;
                                    top: 200px;

                                   """):
        chart1 = ui.highchart({
            'chart': {
                'type': 'line',
            },
            'title': {
                'text': 'Temperature Over Time',
            },
            'xAxis': {
                'type': 'datetime',
                'title': {
                    'text': 'Time'
                }
            },
            'yAxis': {
                'title': {
                    'text': 'Temperature (°C)'
                }
            },
            'series': [{
                'name': 'Temperature',
                'data': Temperature,
                'tooltip': {
                    'valueSuffix': ' °C'
                }
            }]
        }).style("width: 500px; height: 200px;")
        chart1 = ui.highchart({
            'chart': {
                'type': 'line',
            },
            'title': {
                'text': 'Acceleration Over Time',
            },
            'xAxis': {
                'type': 'datetime',
                'title': {
                    'text': 'Time'
                }
            },
            'yAxis': {
                'title': {
                    'text': 'Acceleration (m/s^2)'
                }
            },
            'series': [{
                'name': 'Temperature',
                'data': Temperature,
                'tooltip': {
                    'valueSuffix': ' °C'
                }
            }]
        }).style("width: 500px; height: 200px;")
        chart1 = ui.highchart({
            'chart': {
                'type': 'line',
            },
            'title': {
                'text': 'Altitude Over Time',
            },
            'xAxis': {
                'type': 'datetime',
                'title': {
                    'text': 'Time'
                }
            },
            'yAxis': {
                'title': {
                    'text': 'Altitude (m)'
                }
            },
            'series': [{
                'name': 'Temperature',
                'data': Temperature,
                'tooltip': {
                    'valueSuffix': ' °C'
                }
            }]
        }).style("width: 500px; height: 200px;")
        chart1 = ui.highchart({
            'chart': {
                'type': 'line',
            },
            'title': {
                'text': 'Angular Rate Over Time',
            },
            'xAxis': {
                'type': 'datetime',
                'title': {
                    'text': 'Time'
                }
            },
            'yAxis': {
                'title': {
                    'text': 'Angular Rate (deg/s)'
                }
            },
            'series': [{
                'name': 'Temperature',
                'data': Temperature,
                'tooltip': {
                    'valueSuffix': ' °C'
                }
            }]
        }).style("width: 500px; height: 200px;")
        chart1 = ui.highchart({
            'chart': {
                'type': 'line',
            },
            'title': {
                'text': 'Magnetic Field Over Time',
            },
            'xAxis': {
                'type': 'datetime',
                'title': {
                    'text': 'Time'
                }
            },
            'yAxis': {
                'title': {
                    'text': 'Magnetic Field (uT)'
                }
            },
            'series': [{
                'name': 'Temperature',
                'data': Temperature,
                'tooltip': {
                    'valueSuffix': ' °C'
                }
            }]
        }).style("width: 500px; height: 200px;")
def Graph(ind):
     with ui.card().style("""
                            position: absolute;
                            left: 200px;
                            top: 200px;
                            """,
                            ):
            with ui.row():
                chart = ui.highchart({
            'chart': {
                'type': 'line',
            },
            'title': {
                'text': 'Temperature Over Time',
            },
            'xAxis': {
                'type': 'datetime',
                'title': {
                    'text': 'Time'
                }
            },
            'yAxis': {
                'title': {
                    'text': 'Temperature (°C)'
                }
            },
            'series': [{
                'name': 'Temperature',
                'data': Temperature,
                'tooltip': {
                    'valueSuffix': ' °C'
                }
            }]
        }).style("width: 700px; height: 500px;")
                with ui.card().style("position: relative; left: 250px; top: 10px;width: 200px; height: 400px;background-color: #727472"):
                    with ui.column():
                        with ui.card().style("""
                                            width: 180px;
                                            height: 150px;
                                            background-color: black;
                                            """):
                            with ui.column().style("""
                                                width: 100%
                                                """):
                                ui.label("STATUS").style("""
                                                        color: white;
                                                        font-size: 20px;
                                                        font-weight: bold;
                                                        text-align: center;
                                                        """)
                            
                                ui.label("OK").style("""
                                                        color: red;
                                                        font-size: 50px;
                                                        font-weight: bold;
                                                        text-align: center;
                                                        """)
                    with ui.card().style("""
                                            width: 180px;
                                            height: 150px;
                                            background-color: black;
                                            """):
                        with ui.column().style("""
                                                width: 100%
                                                """):
                            ui.label("TEMPERATURE").style("""
                                                        color: white;
                                                        font-size: 20px;
                                                        font-weight: bold;
                                                        text-align: center;
                                                        """)
                            
                            ui.label(f"{Temperature[ind]} °C").style("""
                                                        color: red;
                                                        font-size: 20px;
                                                        font-weight: bold;
                                                        text-align: center;
                                                        """)

def simulation():
            global enable
            global sim_controls_column
            if not state['displayed']:
                # Show controls
                state['displayed'] = True

                with ui.column() as sim_controls_column:

                    def enable_sim():
                        global enable
                        enable = True
                        ui.notify("Simulation Enabled")

                    def activate_sim():
                        if enable:
                            ui.notify("Simulation Activated")
                        else:
                            ui.notify("Please ENABLE the simulation first")

                    ui.label('ENABLE')\
                        .on('click', enable_sim)\
                        .style(
                            '''
                            align-self: end;
                            background-color: red;
                            color: white;
                            padding: 10px 20px;
                            border-radius: 6px;
                            font-weight: bold;
                            font-size: 16px;
                            cursor: pointer;
                            position: absolute;
                            top: 100px;
                            left: 90%;
                            '''
                        )

                    ui.label('ACTIVATE')\
                        .on('click', activate_sim)\
                        .tooltip('First Enable the Simulation then activate it')\
                        .style(
                            '''
                            align-self: end;
                            background-color: red;
                            color: white;
                            padding: 10px 20px;
                            border-radius: 6px;
                            font-weight: bold;
                            font-size: 16px;
                            cursor: pointer;
                            position: absolute;
                            top: 150px;
                            left: 90%;
                            '''
                        )

            else:
                # Hide controls
                if sim_controls_column:
                    sim_controls_column.clear()
                state['displayed'] = False

        # # === SIMULATION BUTTON ===
        # side_bar()
        # def side_bar():



def simulation_button():
            ui.label('Start Simulation').on('click', simulation).style(
                '''
                background-color: red;
                color: white;
                padding: 10px 20px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 16px;
                cursor: pointer;
                text-align: center;
                position: absolute;
                top: 60px;
                left: 90%;
                transform: translate(-50%, -50%);
                '''
            )
@ui.page('/AllCharts')
def allCharts():
        ui.add_css("""
            body {
                background-color: black;
                color: white;
            }
        """)

        # === HEADER BAR ===
        with ui.row().style("background-color: #4b5563; color: white; height: 100px; width: 100%; justify-content: center; align-items: center;"):

            ui.image("./assets/Logo.png").style("""
                                                position: absolute;
                                                width: 100px;
                                                height: 100px;
                                                top: 10px;
                                                left: 50px;
                                                """)
            # with ui.fab('menu').style("left: 20px; position: absolute;"):
            #     with ui.fab_action('map', on_click=lambda: ui.notify('You are viewing Map')):
            #         ui.tooltip("View Map")
            #     with ui.fab_action('insights', on_click=lambda: ui.notify('Telemetry Logs')):
            #         ui.tooltip("View Logs")
            #     with ui.fab_action('article', on_click=lambda: ui.notify('Save CSV')):
            #         ui.tooltip("Save CSV")
            with ui.column():
                ui.label("TEAM SAMMARD").style("font-size: 24px; font-weight: bold;padding-left: 10px;align-self: center;")
                ui.label("GROUND CONTROL SYSTEM").style("font-size: 24px; font-weight: bold;")
            simulation_button()

        # === SIMULATION CONTROL TOGGLE STATE ===
        ui.column().style("background-color: #111827; height: 100vh; width: 150px; top: 100px; padding-top: 20px;")
        # === SIMULATION TOGGLE FUNCTION ===
        index = 0
        def show_home():
            home.home()
        def show_intern_temp():
            intern_temp.int_temp()
        def draw():
            global index
            coords = latlngs[index]
            index+=1
        def handle_draw():
            ui.timer(draw,1000)
        def Timer():
            ui.link('/page')
        with ui.row().style("height: 10px").style("position: absolute; top: 130px; left: 180px"):
            # ui.button("Home").on_click(lambda: ui.navigate_to('/home'))
            ui.link("Home",'/').style(
        'background-color: #3B82F6; '  # Tailwind's bg-blue-500
        'color: white; '
        'font-weight: bold; '
        'padding: 8px 16px; '
        'border-radius: 6px; '
        'text-decoration: none; '
        'display: inline-block; '
        'transition: background-color 0.2s ease-in-out;'
    )
            ui.link("Internal Temperature", '/intern_temp').style(
        'background-color: #3B82F6; '  # Tailwind's bg-blue-500
        'color: white; '
        'font-weight: bold; '
        'padding: 8px 16px; '
        'border-radius: 6px; '
        'text-decoration: none; '
        'display: inline-block; '
        'transition: background-color 0.2s ease-in-out;'
    )

            ui.link("Altitude",'/altitude').style(
        'background-color: #3B82F6; '  # Tailwind's bg-blue-500
        'color: white; '
        'font-weight: bold; '
        'padding: 8px 16px; '
        'border-radius: 6px; '
        'text-decoration: none; '
        'display: inline-block; '
        'transition: background-color 0.2s ease-in-out;'
    )
            ui.link("Acceleration",'/acceleration').style(
        'background-color: #3B82F6; '  # Tailwind's bg-blue-500
        'color: white; '
        'font-weight: bold; '
        'padding: 8px 16px; '
        'border-radius: 6px; '
        'text-decoration: none; '
        'display: inline-block; '
        'transition: background-color 0.2s ease-in-out;'
    )
            ui.link("Angular rate",'/angularRate').style(
        'background-color: #3B82F6; '  # Tailwind's bg-blue-500
        'color: white; '
        'font-weight: bold; '
        'padding: 8px 16px; '
        'border-radius: 6px; '
        'text-decoration: none; '
        'display: inline-block; '
        'transition: background-color 0.2s ease-in-out;'
    )
            ui.link("Magnetic field",'/magneticField').style(
        'background-color: #3B82F6; '  # Tailwind's bg-blue-500
        'color: white; '
        'font-weight: bold; '
        'padding: 8px 16px; '
        'border-radius: 6px; '
        'text-decoration: none; '
        'display: inline-block; '
        'transition: background-color 0.2s ease-in-out;'
    )
            ui.link("Map",'/map').style(
        'background-color: #3B82F6; '  # Tailwind's bg-blue-500
        'color: white; '
        'font-weight: bold; '
        'padding: 8px 16px; '
        'border-radius: 6px; '
        'text-decoration: none; '
        'display: inline-block; '
        'transition: background-color 0.2s ease-in-out;'
    )
            ui.link("Live Video",'/liveVideo').style(
        'background-color: #3B82F6; '  # Tailwind's bg-blue-500
        'color: white; '
        'font-weight: bold; '
        'padding: 8px 16px; '
        'border-radius: 6px; '
        'text-decoration: none; '
        'display: inline-block; '
        'transition: background-color 0.2s ease-in-out;'
    )
            ui.link("All Charts",'/AllCharts').style(
    'background-color: #3B82F6; '  # Tailwind's bg-blue-500
    'color: white; '
    'font-weight: bold; '
    'padding: 8px 16px; '
    'border-radius: 6px; '
    'text-decoration: none; '
    'display: inline-block; '
    'transition: background-color 0.2s ease-in-out;'
)
        ind = 0
        # Graph(ind)
        charts()
