import {useState} from "react";
import {apiClient} from "../clients/apiClient.jsx";

export function Quiz({ id, data, setQuizData }) {
    const [selectedAnswer, setSelectedAnswer] = useState(null);
    const [isSubmitted, setIsSubmitted] = useState(false);
    const [loading, setLoading] = useState(false);


    const handleSelectAnswer = (index, isCorrect) => {
        setSelectedAnswer({index, isCorrect});
        setIsSubmitted(false);
    };
    const handleSubmit = () => {
        if (!selectedAnswer) return;
        setIsSubmitted(true);
    };
    const handleGenerateNewQuiz = () => {
        setSelectedAnswer(null);
        setIsSubmitted(false);
        setLoading(true)
        apiClient.post(`/gpt/${id}`, {quiz: data.quiz.q})
            .then(response => {
                setQuizData(response.data);
                setLoading(false)
            })
            .catch(error => {
                setLoading(false)
                console.error("Eroare la generarea unui nou quiz:", error);
            });
    };
    if (loading) {
        return <div className="grid place-items-center w-full h-full">
            <h2 className="text-center text-2xl/9 font-bold tracking-tight text-gray-900">
                Se încarcă...</h2>
        </div>;
    }
    return (
        <div className="p-7 shadow-md rounded-2xl sm:mx-auto sm:w-full sm:max-w-md space-y-6 flex flex-col gap-4">
            <h2 className="text-center text-2xl/9 font-bold tracking-tight text-gray-900 ">{data.quiz.q}</h2>
                <div className="flex flex-col gap-4">
                    {data && data.quiz.a.map((answer, index) => {
                        const isSelected = selectedAnswer?.index === index;

                        let bgColor = "bg-gray-200 text-gray-900";
                        if (isSubmitted && isSelected) {
                            bgColor = selectedAnswer.isCorrect
                                ? "bg-green-500 text-white"
                                : "bg-red-500 text-white";
                        } else if (isSelected) {
                            bgColor = "bg-indigo-300 text-white";
                        }
                        return (
                            <div key={index}>
                                <input
                                    type="checkbox"
                                    id={`answer-${index}`}
                                    className="hidden"
                                    checked={selectedAnswer?.index === index}
                                    onChange={()=>{}}
                                />
                                <label
                                    htmlFor={`answer-${index}`}
                                    className={`block w-full px-3 py-1.5 rounded-md  text-sm/6 cursor-pointer transition-colors duration-300 ${bgColor}`}
                                    onClick={() => handleSelectAnswer(index, answer.s)}
                                >
                                    {answer.v}
                                </label>

                            </div>
                        );
                    })}
                    <button type="button"
                            className={`flex w-full justify-center rounded-md px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs  focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600
                                        ${
                                selectedAnswer
                                    ? 'bg-blue-600 hover:bg-blue-700 cursor-pointer text-white'
                                    : 'bg-gray-400 cursor-not-allowed text-gray-700'
                            }`}
                            onClick={isSubmitted ? handleGenerateNewQuiz : handleSubmit}
                            disabled={!selectedAnswer}>
                        {isSubmitted ? "Generează" : "Verifică răspunsul"}

                    </button>
                </div>
        </div>
    );
}