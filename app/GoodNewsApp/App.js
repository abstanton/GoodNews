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
              <Drawer.Screen name="All" component={FeedScreen} initialParams={{section: "all"}}/>
              <Drawer.Screen name="Politics" component={FeedScreen} initialParams={{section: "politics"}}/>
              <Drawer.Screen name="Sports" component={FeedScreen} initialParams={{section: "sports"}}/>
              <Drawer.Screen name="Technology" component={FeedScreen} initialParams={{section: "technology"}}/>
            </Drawer.Navigator>
          </NavigationContainer>
        </SafeAreaView>
      </PaperProvider>
    </SafeAreaProvider>

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
AppRegistry.registerComponent(appName, () => Main)