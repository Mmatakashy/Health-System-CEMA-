import React from 'react';
import { Separator } from '@chakra-ui/react';
import {
  Box,
  Container,
  Heading,
  Text,
  Button,
  SimpleGrid,
  Card,
  CardBody,
  Stack,
  Link,
  Divider,
  VStack
} from '@chakra-ui/react';

function App() {
  return (
    <Box>
      {/* Header Section */}
      <Box bg="teal.500" color="white" p={5}>
        <Container maxW="container.lg">
          <Heading as="h1" size="xl">
            Health System
          </Heading>
        </Container>
      </Box>

      {/* News Section */}
      <Container maxW="container.lg" my={10}>
        <Heading as="h2" size="lg" mb={4}>
          Latest News
        </Heading>
        <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} spacing={10}>
          <Card>
            <CardBody>
              <Heading size="md">News Article 1</Heading>
              <Text mt={2}>
                Short description or teaser for the news article.
              </Text>
              <Button colorScheme="teal" size="sm" mt={3}>
                Read More
              </Button>
            </CardBody>
          </Card>
          <Card>
            <CardBody>
              <Heading size="md">News Article 2</Heading>
              <Text mt={2}>
                Another brief description of the second news article.
              </Text>
              <Button colorScheme="teal" size="sm" mt={3}>
                Read More
              </Button>
            </CardBody>
          </Card>
          <Card>
            <CardBody>
              <Heading size="md">News Article 3</Heading>
              <Text mt={2}>
                A quick summary of what this news is about.
              </Text>
              <Button colorScheme="teal" size="sm" mt={3}>
                Read More
              </Button>
            </CardBody>
          </Card>
        </SimpleGrid>
      </Container>

      {/* Quick Links Section */}
      <Box bg="gray.100" py={10}>
        <Container maxW="container.lg">
          <Heading as="h2" size="lg" mb={4}>
            Quick Links
          </Heading>
          <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} spacing={10}>
            <Box>
              <Heading size="md">Contact</Heading>
              <Text mt={2}>Get in touch with us for inquiries or support.</Text>
              <Button colorScheme="teal" size="sm" mt={3}>
                Contact Us
              </Button>
            </Box>
            <Box>
              <Heading size="md">About Us</Heading>
              <Text mt={2}>Learn more about our mission and values.</Text>
              <Button colorScheme="teal" size="sm" mt={3}>
                Read More
              </Button>
            </Box>
            <Box>
              <Heading size="md">Services</Heading>
              <Text mt={2}>Discover the services we provide to the community.</Text>
              <Button colorScheme="teal" size="sm" mt={3}>
                View Services
              </Button>
            </Box>
          </SimpleGrid>
        </Container>
      </Box>

      {/* Footer Section */}
      <Box bg="teal.500" color="white" py={5}>
        <Container maxW="container.lg">
          <VStack spacing={3}>
            <Text>© 2025 Health System. All rights reserved.</Text>
            <Divider />
            <Stack direction="row" spacing={5}>
              <Link href="https://facebook.com" isExternal>
                Facebook
              </Link>
              <Link href="https://twitter.com" isExternal>
                Twitter
              </Link>
              <Link href="https://instagram.com" isExternal>
                Instagram
              </Link>
            </Stack>
          </VStack>
        </Container>
      </Box>
    </Box>
  );
}

export default App;
