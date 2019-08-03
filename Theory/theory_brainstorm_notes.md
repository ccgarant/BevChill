# Theory Brainstorm Notes

## Theory
Important variables for heat transfer are are:
- Fluid Properites (heat capacity, specific density(ies))
- Container properties (geometry, material)
- Ambient environmental temperature
- Time steps
- Coeffiecients of heat transfer (convection and radiation)

Variables to predict
- Internal beer temperature
- Predicted times for temperature

## Structure
The code structure / architecture
- chill_plot(Temp,time) = visualization
- chill_timer(beverage, T_bev_initial, T_freezer_initial) = Temp, time
    - beverage 
        - beverage_beer
            - beer(x,y,z)
        - beverage_container
            - container(r_outter,r_inner)
            
            
    - beverage(perroni_bottle)
        - beverage_beer(perroni_beer)
            - beer.density = perroni['density']
        - beverage_bottle (perroni_bottle = container(r_outter,r_inner))
            - container(r_outter,r_inner)  
            
               
- chill_timer(beverage, T_bev_initial, T_freezer_initial) = Temp, time
    - bev = beverage
    - bev.beer.density
    - bev.container.density
    


## Details
- chill_timer(beverage, T_bev_initial, T_freezer_initial) = Temp, time
    - returns the time it will take to reach the ideal drinking temperature
    - sets the timer to run and predicts the current temperature
    - display the temp vs time graph, color coded intervals between, warm, good enough, good, best, ideal, frozen
    - beverage_name
        - class beer fluid properties
    - beverage_container
        - class bottle container
        - class can container
    - physics solver
        - solvers the heat transfer equation problem