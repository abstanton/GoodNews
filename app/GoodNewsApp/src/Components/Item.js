import React from 'react'
import {Text, Card, Title, Paragraph} from 'react-native-paper'
import {Image, StyleSheet,View} from 'react-native'

export default class Item extends React.Component{
    render(){
        return(
            <View style={{margin: 10}}>
            <Card elevation={3}>
                {this.renderImage()}
                <Card.Content>
                    <Title>{this.props.article.title}</Title>
                    <Paragraph>{this.props.article.description}</Paragraph>
                </Card.Content>                
            </Card>
            </View>
        );
    }

    renderImage(){
        if(this.props.article.urlToImage){
            return(<Card.Cover source={{uri: this.props.article.urlToImage}}/>)
        }
        else{
            return
        }
    }
}

const styles = StyleSheet.create({
    cardStyle: {

    }
})