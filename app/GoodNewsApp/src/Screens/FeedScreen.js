import React from 'react';
import {TextInput} from 'react-native-paper';
import { StyleSheet, View, Platform, StatusBar } from 'react-native';
import List from './../Components/List'


export default function FeedScreen({route, Navigation}){
    return(
    <View>
        <TextInput
            label="Search"

        />
        <List style={{width: '90%'}} category={route.name}/>
    </View>

    );
    
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'center',
    },
    AndroidSafeArea: {
      flex: 1,
      backgroundColor: "white",
      paddingTop: Platform.OS === "android" ? StatusBar.currentHeight : 0
    },
  });
