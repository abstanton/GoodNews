import React from 'react'
import {Text} from 'react-native-paper'
import { FlatList, View, StyleSheet } from 'react-native'
import Item from './Item'

export default class List extends React.PureComponent{
    state = {
        articles: [],
        articlesToDisplay: []
    }

    listCallback= (value) => {
        this.props.parentCallback(value)
    }

    render(){
        return(
            <FlatList
            data={this.props.articles}
            renderItem={({item}) => (
                <Item article={item} parentCallback={this.listCallback} sentiment={this.props.sentiment}/>
            )}
            keyExtractor={item => {
                
                return item.id.toString()
            }}
            contentContainerStyle={{paddingBottom: 400}}
            />
        )
    }
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