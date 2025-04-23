<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="20008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="CRONUS-2P VIs" Type="Folder">
			<Item Name="Close Shutter.vi" Type="VI" URL="../Close Shutter.vi"/>
			<Item Name="Get Channel Status.vi" Type="VI" URL="../Get Channel Status.vi"/>
			<Item Name="Get Wavelength Setting State.vi" Type="VI" URL="../Get Wavelength Setting State.vi"/>
			<Item Name="Get Wavelength.vi" Type="VI" URL="../Get Wavelength.vi"/>
			<Item Name="Laser Parameters.vi" Type="VI" URL="../Laser Parameters.vi"/>
			<Item Name="Open Shutter.vi" Type="VI" URL="../Open Shutter.vi"/>
			<Item Name="Set Channel Wavelength.vi" Type="VI" URL="../Set Channel Wavelength.vi"/>
			<Item Name="Wait For Wavelength Change.vi" Type="VI" URL="../Wait For Wavelength Change.vi"/>
		</Item>
		<Item Name="REST API" Type="Folder">
			<Item Name="Endpoint Format.vi" Type="VI" URL="../Endpoint Format.vi"/>
			<Item Name="HTTP Get.vi" Type="VI" URL="../HTTP Get.vi"/>
			<Item Name="HTTP Post.vi" Type="VI" URL="../HTTP Post.vi"/>
			<Item Name="HTTP Put.vi" Type="VI" URL="../HTTP Put.vi"/>
			<Item Name="HTTP URL Format.vi" Type="VI" URL="../HTTP URL Format.vi"/>
		</Item>
		<Item Name="Basic Example.vi" Type="VI" URL="../Basic Example.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="LabVIEWHTTPClient.lvlib" Type="Library" URL="/&lt;vilib&gt;/httpClient/LabVIEWHTTPClient.lvlib"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="NI_PackedLibraryUtility.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/LVLibp/NI_PackedLibraryUtility.lvlib"/>
				<Item Name="Path To Command Line String.vi" Type="VI" URL="/&lt;vilib&gt;/AdvancedString/Path To Command Line String.vi"/>
				<Item Name="PathToUNIXPathString.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/CFURL.llb/PathToUNIXPathString.vi"/>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
