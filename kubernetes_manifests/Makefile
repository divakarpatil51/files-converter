deploy-application-stack:
	kubectl apply -f base_setup/. && \
	cd auth_service && \
	${MAKE} deploy-auth-stack && \
	cd ../api_gateway && \
	${MAKE} deploy-api-gw-stack


undeploy-application-stack:
	kubectl delete namespace files-converter-app