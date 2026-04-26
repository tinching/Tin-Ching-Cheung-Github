install.packages(c("shiny", "ggplot2", "dplyr", "sf"))

library(shiny)
library(ggplot2)
library(dplyr)
library(sf)

ni <- read_sf("geography-sdz2021-esri-shapefile/SDZ2021.shp")

ui<-fluidPage(
  
  selectInput(
    inputId='district',
    label='Choose a Local Government District:',
    choices=unique(ni$LGD2014_nm)
    ),
  fluidRow(
    column(width=6,plotOutput('map')),
    column(width=6,plotOutput('scatter'))
    )
  )
server<-function(input,output){
  
  selected_data<-reactive({
    filter(ni,LGD2014_nm==input$district)
  })
  
  output$map<-renderPlot({
    ggplot()+
      geom_sf(data=ni, color='grey')+
      geom_sf(data=selected_data(), aes(fill=Perim_km), color=NA)+
      labs(title=input$district, fill='Perimeter(km)', x='Longitude', y='Latitude')
  })
  output$scatter<-renderPlot({
    ggplot(data=selected_data(), aes(x=Perim_km,y=Area_ha))+
      geom_point()+
      labs(title=input$district, x='Perimeter(km)', y='Area(hectare)')
    })
}
shinyApp(ui=ui,server=server)


