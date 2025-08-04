def main ():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance": 0.01, "Orbit": "Sun"})
    print(create_report(spacecraft))  

def create_report(spacecraft):
    return f"""
    ============REPORT============

    Name: {spacecraft.get("name", "unknown")}
    Distance: {spacecraft.get("distance", "unknown")} AU
    Orbit: {spacecraft.get("Orbit", "unknown")}

    ==============================
    """

main()