import React from 'react'
import {Text, Card, Title, Paragraph} from 'react-native-paper'
import {Image, StyleSheet,View} from 'react-native'

export default class Item extends React.Component{
    sentimentScore=((this.props.article.sentiment_score+1) * 5).toFixed(1)        
    senderData = (value) => {
        this.props.parentCallback(value)
        console.log(value)
        
    }
    
    render(){
        
        return(
            <View style={{marginBottom: 10, marginLeft:10, marginRight:10}}>
            <Card elevation={3} onPress={() => this.senderData(this.props.article.url)}>
                {this.renderImage()}
                <Card.Content>
                    <Title>{this.props.article.title}</Title>
                    <View style={{flex: 1, flexDirection:"row", justifyContent: "space-between", alignItems: "center"}}>
                    <Paragraph style={{width: '85%'}}>{this.props.article.description} </Paragraph>
                    <View>
                    <Paragraph style={this.scoreStyle()}>{this.sentimentScore}</Paragraph>

                    </View>
                    </View>
                </Card.Content>                
            </Card>
            </View>
        );
    }

    scoreStyle = function(options){
        return {
            fontSize: 20,
            fontWeight: 'bold',
            color: this.getColor(1-this.sentimentScore/10)
        }
    }

    getColor(value){
        //value from 0 to 1
        var hue=((1-value)*120).toString(10);
        return ["hsl(",hue,",100%,50%)"].join("");
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