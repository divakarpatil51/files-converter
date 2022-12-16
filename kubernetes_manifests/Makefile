deploy-application-stack:
	kubectl apply -f base_setup/. && \
	cd auth_service && \
	${MAKE} deploy-auth-stack


undeploy-application-stack:
	kubectl delete namespace files-converter-app