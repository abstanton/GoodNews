import React from 'react'
import {Text, Slider, View} from 'react-native'

export default class Footer extends React.Component{
    senderData = (value) => {
        this.props.parentCallback(value)
    }

    render(){
        return(
            <View>
                <Slider
                maximumValue={1}
                minimumValue={-1}
                value={-1}
                onValueChange={val => this.senderData(val)}
                />
            </View>
        )
    }
}