import React from 'react';
import {AppRegistry} from 'react-native';
import {Provider as PaperProvider, Button} from 'react-native-paper';
import { StyleSheet, Text, View } from 'react-native';
import {name as appName} from './app.json'
import {SafeAreaProvider} from 'react-native-safe-area-context';
import SafeAreaView from 'react-native-safe-area-view';

export default function App() {
  return (
    
      
        <PaperProvider>
          <SafeAreaProvider>
          <SafeAreaView>
          <Button icon="camera">press me</Button>
          </SafeAreaView>
          </SafeAreaProvider>
        </PaperProvider>
      
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
AppRegistry.registerComponent(appName, () => Main)