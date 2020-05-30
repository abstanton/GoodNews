import React from 'react';
import {TextInput} from 'react-native-paper';
import { StyleSheet, View, Platform, StatusBar, ScrollView } from 'react-native';
import List from './../Components/List'
import Scroll from './../Components/Scroll'
import axios from 'axios'

export default class FeedScreen extends React.Component{
    state = {sentiment: -1, articles: []}
    render(){
        
        return(
        <View>
            <View>
            <TextInput
                label="Search"

            />
            <Scroll parentCallback={this.callBackFunction}/>
            <List style={{width: '90%'}} articles={this.state.articles.filter(article => article.sentiment_score > this.state.sentiment)} sentiment={this.state.sentiment}/>
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
            axios.get(url)
            .then(res => {                
                this.setState({articles: res.data})
            })
            return
        }
        else if(this.props.route.name == 'Politics'){
            url = "http://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=politics&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
        }
        else if(this.props.route.name == 'Sports'){
            url = "http://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=sports&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
        }
        else if(this.props.route.name == 'Technology'){
            url = "http://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=technology&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
        }
        
        fetch(url)
            .then(res => res.json())
            .then(data => {
                this.setState({articles: data['articles']})            
            })
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
