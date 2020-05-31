import React from 'react'
import {WebView} from 'react-native-webview'

export default class Browser extends React.Component{
    static navigationOptions = {
        drawerLabel: () => null
    }
    //url = this.props.route.params.url
    render() {
        console.log(this.props)
        return(
            <WebView source={{uri:this.props.route.params["url"]}}/>
        )
    }
}