# ParkFacilitiesSearching  
This project utilizes a GUI to allow students in Vancouver to select their school and preferred park facility, subsequently filtering and analyzing park data to present the three closest parks with the desired facility, including a terminal display of all facilities, along with a bar graph highlighting the selected facility among the park amenities.  

# Tech Stack  
• Developed a **python** based student park facilities searching GUI app  
• Extracted, loaded, and analyzed data from the Vancouver Open Data project (https://opendata.vancouver.ca/pages/home/) to obtain relevant information  
• Designed and implemented a user-friendly GUI using **Tkinter** and a visualization dashboard using **Matplotlib**, allowing students to search for the closest three parks with their schools and requested facilities  
• Conducted thorough testing of all functions and classes using **unittest** to ensure the reliability and robustness  

# Demo Screenshots:  
Run the **data_dashboard.py** file to start the program  
  
Users can select their school and desired facility from dropdown lists:  
![Alt text](./demo%20pictures/GUI.png)  

After the users make selections, the dashboard appears, displaying the three closest parks with the available facility as below (e.g., 'Children's Hearing and Speech Centre BC' and 'field houses'):  
![Alt text](./demo%20pictures/dashboard.png)  

Simultaneously, detailed information appears in the terminal, providing comprehensive insights into all facilities available at these three parks: 
![Alt text](./demo%20pictures/terminal%20info.png)