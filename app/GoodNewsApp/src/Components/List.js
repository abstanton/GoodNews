import React from 'react'
import {Text} from 'react-native-paper'
import { FlatList, Image, View } from 'react-native'
import Item from './Item'

export default class List extends React.Component{
    state = {
        articles: []
    }
    render(){
        return(
            
            <FlatList
            data={this.state.articles}
            renderItem={({item}) => (
                <Item article={item}/>
            )}
            keyExtractor={item => item.url}
            />
        )
    }
    componentDidMount(){
        let url = ""
        if(this.props.category == 'All'){
            url = "https://newsapi.org/v2/top-headlines?pageSize=100&language=en&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
        }
        else if(this.props.category == 'Politics'){
            url = "http://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=politics&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
        }
        else if(this.props.category == 'Sports'){
            url = "http://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=sports&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
        }
        else if(this.props.category == 'Technology'){
            url = "http://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=technology&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
        }
        
        fetch(url)
            .then(res => res.json())
            .then(data => {
                this.setState({articles: data['articles']})            
            })
    }
}