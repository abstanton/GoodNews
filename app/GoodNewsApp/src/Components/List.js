import React from 'react'
import {Text} from 'react-native-paper'
import { FlatList, View, StyleSheet } from 'react-native'
import Item from './Item'
import axios from 'axios'

export default class List extends React.PureComponent{
    state = {
        articles: [],
        articlesToDisplay: []
    }

    handleChange = event => {
        this.setState
    }

    render(){
        return(
            
            <FlatList
            data={this.props.articles}
            renderItem={({item}) => (
                <Item article={item} sentiment={this.props.sentiment}/>
            )}
            keyExtractor={item => item.url}
            />
        )
    }
    

    // componentDidMount(){
    //     let url = ""
    //     if(this.props.category == 'All'){
    //         url = "http://192.168.1.33:5000/news/all"
    //         axios.get(url)
    //         .then(res => {                
    //             this.setState({articles: res.data})
    //         })
    //         return
    //     }
    //     else if(this.props.category == 'Politics'){
    //         url = "http://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=politics&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
    //     }
    //     else if(this.props.category == 'Sports'){
    //         url = "http://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=sports&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
    //     }
    //     else if(this.props.category == 'Technology'){
    //         url = "http://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=technology&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
    //     }
        
    //     fetch(url)
    //         .then(res => res.json())
    //         .then(data => {
    //             this.setState({articles: data['articles']})            
    //         })
    // }
}
const styles = StyleSheet.create({
    headerStyle: {
        flex: 1,
        height: 40,
        width: '100%',
        backgroundColor: 'blue',
        justifyContent: 'center',
        alignItems: 'center',
        },
})