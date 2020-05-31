import 'react-native-gesture-handler';
import React from 'react';
import {AppRegistry} from 'react-native';
import {Provider as PaperProvider, Button, Card, DefaultTheme, DarkTheme} from 'react-native-paper';
import { StyleSheet, Text, View, Platform, StatusBar } from 'react-native';
import {name as appName} from './app.json'
import {SafeAreaProvider} from 'react-native-safe-area-context';
import SafeAreaView from 'react-native-safe-area-view';
import List from './src/Components/List'
import {NavigationContainer} from '@react-navigation/native';
import{createDrawerNavigator} from '@react-navigation/drawer';
import FeedScreen from './src/Screens/FeedScreen'
import Browser from './src/Screens/Browser';


const theme = {
  ...DefaultTheme,
  roundness: 2,
  colors: {
    ...DefaultTheme.colors,

  },
};

const Drawer = createDrawerNavigator();

export default function App() {
  return (
    <SafeAreaProvider>
      <PaperProvider>
        <SafeAreaView style = {styles.AndroidSafeArea}>
          <NavigationContainer>
            <Drawer.Navigator initialRouteName="All">
              <Drawer.Screen name="All" component={FeedScreen}/>
              <Drawer.Screen name="General" component={FeedScreen}/>
              <Drawer.Screen name="Sports" component={FeedScreen}/>
              <Drawer.Screen name="Tech" component={FeedScreen}/>
              <Drawer.Screen name="Science" component={FeedScreen} />
              <Drawer.Screen name="Health" component={FeedScreen}/>
              <Drawer.Screen name="Business" component={FeedScreen} />
              <Drawer.Screen name="Entertainment " component={FeedScreen} />
              <Drawer.Screen name=" " component={Browser} />

            </Drawer.Navigator>
          </NavigationContainer>
        </SafeAreaView>
      </PaperProvider>
    </SafeAreaProvider>

  );
}

function hidden(){
  return null
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
AppRegistry.registerComponent(appName, () => Main)