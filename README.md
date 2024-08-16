<h1 align="center">
  Delivery Routing Simulator
  <br>
</h1>

<h4 align="center">A Python script designed to formulate an optimal logistics route for package delivery </h4>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#constraints">Constraints</a> •
  <a href="#links">Links</a>
</p>

<p> Delivery Routing Simulator was designed to satisfy curriculum requirements in my computer science degree program.</p> 
<p>The algorithm's purpose is to route delivery trucks in a reasonably optimal path, record delivery times and distances traveled, and meet all other specified constraints.</p>
<p>Delivery Routing Simulator is not currently under active development</p>


## Features
* Determines and records travel path, total distance traveled, and delivery times for 3 trucks delivering packages simultaneously.
  - Distances between addresses are provided by a reference table, and time is calculated with an assumed average 18 miles per hour.
* Ensures all packages meet their specified delivery deadline.
  - Some packages must be delivered before a specified time, the algorithm ensures that any package with such a constraint is given priority and delivered within the directives.
* Generates detailed reports on specified package or truck upon request, or status of deliveries at a specified time.
* Determines a route well within project guidelines for efficiency.
  - Total truck distance traveled is calculated at 89.4 miles, well below the course's 140 mile maximum requirement.
* Cross platform
  - Windows, Mac OS, and Linux ready

 
## Constraints

* Each truck can carry a maximum of 16 packages.
* Trucks travel at an average speed of 18 miles per hour with no need to stop.
* Total truck travel distance must not be more than 140 miles.
  - (Delivery Routing Simulator determined an actual total of 89.4 total miles)
* Three trucks and two drivers are available for deliveries.
  - A driver may board another truck and commence deliveries once returning to the hub with their first truck.
* Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.
* The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages to a truck at the hub.
* The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. the company is aware that
  the address is incorrect and will be updated to the correct destination at 10:20 a.m.
* The distances provided in the distance table are equal regardless of the direction traveled.


## Links

> [NewtonWill.github.io](https://www.NewtonWill.github.io) &nbsp;&middot;&nbsp;
> GitHub [@NewtonWill](https://github.com/NewtonWill) &nbsp;&middot;&nbsp;
> LinkedIn [William Newton](https://www.linkedin.com/in/william-newton-6203011b9/)
