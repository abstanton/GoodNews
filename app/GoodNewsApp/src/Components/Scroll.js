import React from 'react'
import {Text, Slider, View} from 'react-native'

export default class Footer extends React.Component{
    state = {sentiment: -1}
    senderData = (value) => {
        this.props.parentCallback(value)
    }

    getColor(value){
        //value from 0 to 1
        var hue=((1-value)*120).toString(10);
        return ["hsl(",hue,",100%,50%)"].join("");
    }
    render(){
        return(
            <View>
                <Slider
                minimumTrackTintColor='red'
                maximumTrackTintColor='green'
                thumbTintColor={this.getColor(1-(this.state.sentiment+1)/2)}
                maximumValue={1}
                minimumValue={-1}
                value={-1}
                onValueChange={val => {
                    this.setState({sentiment: val})
                    this.senderData(val)}}
                />
            </View>
        )
    }
}