import React, { useState } from 'react';
import {
  ChakraProvider,
  Box,
  Heading,
  FormControl,
  FormLabel,
  Input,
  Button,
  Text,
  Alert,
  AlertIcon,
} from '@chakra-ui/react';

function App() {
  const [stockPrice, setStockPrice] = useState('');
  const [strikePrice, setStrikePrice] = useState('');
  const [timeToExpiration, setTimeToExpiration] = useState('');
  const [riskFreeRate, setRiskFreeRate] = useState('');
  const [volatility, setVolatility] = useState('');
  const [predicted_value, setpredicted_value] = useState('');
  const [expected_value, setexpected_value] = useState('');
  const [errorMessages, setErrorMessages] = useState({});
  const [outputMessage, setOutputMessage] = useState('');

  const handleChange = (setter) => (e) => {
    setter(e.target.value);
    setOutputMessage('');
  };

  const handlePredict = () => {

    const errors = {
      stockPrice: stockPrice === '',
      strikePrice: strikePrice === '',
      timeToExpiration: timeToExpiration === '',
      riskFreeRate: riskFreeRate === '',
      volatility: volatility === '',
    };

    setErrorMessages(errors);

    if (Object.values(errors).some((error) => error)) {
      setOutputMessage('Please fill in all required fields.');
      setpredicted_value('');
      setexpected_value('');
    } else {
      const inputs = {
        stockPrice: parseFloat(stockPrice),
        strikePrice: parseFloat(strikePrice),
        timeToExpiration: parseFloat(timeToExpiration),
        riskFreeRate: parseFloat(riskFreeRate) / 100,
        volatility: parseFloat(volatility) / 100,
      };
      fetch('https://option-pricing-using-machine-learning-1.onrender.com', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(inputs),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then((data) => {
          console.log('Received response:', data);
          setpredicted_value(data.predicted_value);
          setexpected_value(data.Actual_Value);
          setOutputMessage('');
        })
        .catch((error) => {
          console.error('There was an error!', error);
          setOutputMessage('There was an error with your request.');
        });
    }
  };

  return (
    <ChakraProvider>
      <Box p={5} textAlign="center">
        <Heading as="h1" size="lg">
          Options Price Prediction using Artificial Neural Network
        </Heading>

        {/* Form Container */}
        <Box display="flex" flexDirection="column" alignItems="center" mt={5}>
          {/* Row 1: 2 Inputs */}
          <Box display="flex" mb={2} gap={2} width="80%">
            <FormControl isRequired isInvalid={errorMessages.stockPrice}>
              <FormLabel>Stock Price (S)</FormLabel>
              <Input
                type="text"
                onChange={handleChange(setStockPrice)}
                value={stockPrice}
              />
            </FormControl>
            <FormControl isRequired isInvalid={errorMessages.strikePrice}>
              <FormLabel>Strike Price (K)</FormLabel>
              <Input
                type="text"
                onChange={handleChange(setStrikePrice)}
                value={strikePrice}
              />
            </FormControl>
          </Box>

          {/* Row 2: 2 Inputs */}
          <Box display="flex" mb={2} gap={2} width="80%">
            <FormControl isRequired isInvalid={errorMessages.timeToExpiration}>
              <FormLabel>Time to Expiration (T in Years)</FormLabel>
              <Input
                type="text"
                onChange={handleChange(setTimeToExpiration)}
                value={timeToExpiration}
              />
            </FormControl>
            <FormControl isRequired isInvalid={errorMessages.riskFreeRate}>
              <FormLabel>Risk-Free Rate (r in %)</FormLabel>
              <Input
                type="text"
                onChange={handleChange(setRiskFreeRate)}
                value={riskFreeRate}
              />
            </FormControl>
          </Box>

          {/* Row 3: 1 Centered Input */}
          <FormControl isRequired isInvalid={errorMessages.volatility} width="40%">
            <FormLabel>Volatility (σ in %)</FormLabel>
            <Input
              type="text"
              onChange={handleChange(setVolatility)}
              value={volatility}
            />
          </FormControl>

          {/* Predict Button */}
          <Box mt={4}>
            <Button colorScheme="blue" onClick={handlePredict}>
              Predict
            </Button>
          </Box>

          {/* Output Box */}
          <Box
            borderWidth="1px"
            borderRadius="lg"
            p={4}
            mt={5}
            bg="gray.50"
            textAlign="left"
            width="80%"
            mx="auto" // Center the output box horizontally
          >
            <Heading as="h2" size="md" mb={2}>
              RESULT
            </Heading>
            <Text>Predicted Option Price: Rs.{predicted_value}</Text>
            <Text>Actual Option Price: Rs.{expected_value}</Text>
            {outputMessage && (
              <Alert status="error" mt={4}>
                <AlertIcon />
                {outputMessage}
              </Alert>
            )}
          </Box>
        </Box>
      </Box>
    </ChakraProvider>
  );
}

export default App;
