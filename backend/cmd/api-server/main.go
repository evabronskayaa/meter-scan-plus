package main

import (
	api_service "backend/internal/api-service"
	"backend/internal/config"
	"backend/internal/service"
	"log"
)

func main() {
	var apiConfig config.ApiConfig
	if err := apiConfig.Load(); err != nil {
		log.Panic("Config api load: ", err)
		return
	}

	apiService, err := api_service.NewService(apiConfig)
	if err != nil {
		log.Panic("Get api service: ", err)
		return
	}

	if err := service.StartService(apiService); err != nil {
		return
	}
}
