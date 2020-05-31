import React from 'react';
import {TextInput, Card, Button} from 'react-native-paper';
import { StyleSheet, View, Platform, StatusBar, ScrollView } from 'react-native';
import List from './../Components/List'
import Scroll from './../Components/Scroll'
import axios from 'axios'
import Browser from './Browser';




export default class FeedScreen extends React.Component{
    state = {sentiment: -1, articles: []}
    getColor(value){
        //value from 0 to 1
        var hue=((1-value)*120).toString(10);
        return ["hsl(",hue,",100%,50%)"].join("");
    }

    feedCallback= (uri)=>{
        this.props.navigation.navigate(" ", {'url': uri})
    }

    render(){
        return(
        <View style={{flex: 1}}>
            <View>
            {/* <TextInput
                label="Search"

            /> */}
            <View style={{alignItems: "center"}}>
            <View style={{paddingTop: 20, paddingBottom: 20, width: '90%', justifyContent: "center", backgroundColor: ''}}>
            <Scroll parentCallback={this.callBackFunction}/>
            </View>
            </View>
            <View style={{paddingTop: 10}}>
            <List parentCallback={this.feedCallback} style={{width: '90%'}} articles={this.state.articles.filter(article => article.sentiment_score > this.state.sentiment)} sentiment={this.state.sentiment}/>
            </View>
            </View>
        </View>
        );
    }

    callBackFunction = (childData) => {
        this.setState({sentiment: childData})
    }

    componentDidMount(){
        let url = ""
        if(this.props.route.name == 'All'){
            url = "http://192.168.1.33:5000/news/all"   
        }
        else if(this.props.route.name == 'General'){
            url = "http://192.168.1.33:5000/news/general"
        }
        else if(this.props.route.name == 'Sports'){
            url = "http://192.168.1.33:5000/news/sports"
        }
        else if(this.props.route.name == 'Tech'){
            url = "http://192.168.1.33:5000/news/technology"
        }
        else if(this.props.route.name == 'Science'){
            url = "http://192.168.1.33:5000/news/science"
        }
        else if(this.props.route.name == 'Health'){
            url = "http://192.168.1.33:5000/news/health"
        }
        else if(this.props.route.name == 'Business'){
            url = "http://192.168.1.33:5000/news/business"
        }
        else if(this.props.route.name == 'Entertainment '){
            url = "http://192.168.1.33:5000/news/entertainment"
        }
        
        axios.get(url)
            .then(res => {                
                this.setState({articles: res.data})
            })
        return
    }
    
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'center',
    },
    footerStyle:{
        position: 'absolute', left: 0, right: 0, bottom: 0, top: 0
    },
    AndroidSafeArea: {
      flex: 1,
      backgroundColor: "white",
      paddingTop: Platform.OS === "android" ? StatusBar.currentHeight : 0
    },
  });
