### Liberty as an MCP server

1. Download the beta of [Liberty 25.0.0.11](https://public.dhe.ibm.com/ibmdl/export/pub/software/openliberty/runtime/beta/25.0.0.11-beta/openliberty-25.0.0.11-beta.zip)
2. unzip the code
3. update the pom.xml file with the location of the `wlp` directory
```
<wlp-dir-path>/Applications/IBM/wlp</wlp-dir-path>
```
4. Start the Application Server with maven
```
mvn liberty:start
```
5. Deploy the application
```
mvn liberty:deploy
```
6. Test with the Python Client
