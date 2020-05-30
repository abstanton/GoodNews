import React from 'react'
import {Text, Card, Title, Paragraph} from 'react-native-paper'
import {Image, StyleSheet,View} from 'react-native'

export default class Item extends React.Component{
    render(){
        const sentimentScore=((this.props.article.sentiment_score+1) * 5).toFixed(1)        
        return(
            <View style={{margin: 10}}>
            <Card elevation={3}>
                {this.renderImage()}
                <Card.Content>
                    <Title>{this.props.article.title}</Title>
                    <Paragraph>{this.props.article.description}</Paragraph>
                    <Paragraph>{this.props.sentiment}</Paragraph>
                </Card.Content>                
            </Card>
            </View>
        );
    }

    renderImage(){
        if(this.props.article.url_to_image){
            return(<Card.Cover source={{uri: this.props.article.url_to_image}}/>)
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